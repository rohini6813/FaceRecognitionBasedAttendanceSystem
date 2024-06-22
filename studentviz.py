from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

with open("test.txt",'r') as f:
    student_data = f.read().split(',')


class Studentinfo:
    def __init__(self, root,student_data):
        self.root = root
        self.student_data = student_data
        self.student_id = student_data[4]
        self.root.title("Student Info")
        self.root.geometry("1920x1020+0+0")
        self.root.configure(bg='lightblue')

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)

        # Button to generate the attendance file
        self.generate_and_plot()

    def exit(self):
        self.root.destroy()

        

    def req_file(self):
        # Read the CSV file
        df = pd.read_csv('atd.csv')
        
        # Convert 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
        
        # Filter the DataFrame for dates within the specified range
        start_date = datetime.strptime('01/01/2000', '%d/%m/%Y')
        end_date = datetime.today()
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        
        # Group by specified columns and take the first occurrence of each group
        df_grouped = df.groupby(["Student ID", "Name", "Department", "Semester", "Division", "Teacher", "Subject", "Date"]).first().reset_index()
        
        # Pivot the dataframe to get attendance in date-wise columns
        pivot_df = df_grouped.pivot_table(index=["Student ID", "Name", "Subject"], 
                                          columns='Date', 
                                          values='Attendance', 
                                          aggfunc='first').reset_index()
        
        # Convert 'Date' columns to string format in desired format
        pivot_df.columns = [col.strftime('%d-%B-%Y') if isinstance(col, pd.Timestamp) else col for col in pivot_df.columns]
        
        # Fill NaN values with 'Absent'
        pivot_df.fillna('Absent', inplace=True)

        # Create a new DataFrame for the final output
        student_subject_df = pivot_df.groupby(['Student ID', 'Name', 'Subject']).first().reset_index()
        date_columns = pivot_df.columns[3:]  # Exclude 'Student ID', 'Name', and 'Subject' columns

        # Calculate the attendance percentage per subject
        for subject in student_subject_df['Subject'].unique():
            subject_df = pivot_df[pivot_df['Subject'] == subject]
            subject_attendance_percentage = ((subject_df[date_columns] == 'Present').sum(axis=1) / len(date_columns)) * 100
            student_subject_df.loc[student_subject_df['Subject'] == subject, 'Percentage Attendance'] = subject_attendance_percentage.values

        # Rearrange columns
        output_df = student_subject_df[['Student ID', 'Name', 'Subject'] + list(date_columns) + ['Percentage Attendance']]

        # Create directory if it doesn't exist
        save_directory = 'Attendance_Sheets_2'
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Construct the file path
        file_path = os.path.join(save_directory, 'attendance_data_2.xlsx')
        
        # Export to Excel
        output_df.to_excel(file_path, index=False)
        messagebox.showinfo("Generated", "Attendance Excel Generation is Successfully Done")
        
        return file_path

    def plot_attendance(self, student_id, excel_file):
        # Read the Excel file
        df = pd.read_excel(excel_file)

        # Ensure 'Student ID' is treated as a string and strip any whitespace
        df['Student ID'] = df['Student ID'].astype(str).str.strip()

        # Filter the DataFrame for the specified student ID
        student_df = df[df['Student ID'] == str(student_id).strip()]
        
        # Check if the student ID exists in the data
        if student_df.empty:
            print(f"No data found for Student ID {student_id}")
            return

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.bar(student_df['Subject'], student_df['Percentage Attendance'])
        
        # Adding titles and labels
        plt.title(f'Attendance Percentage for Student ID {student_id}')
        plt.xlabel('Subject')
        plt.ylabel('Percentage Attendance')
        plt.ylim(0, 100)  # Assuming attendance percentage is between 0 and 100
        
        # Display the bar graph
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_and_plot(self):
        # Generate the attendance file
        file_path = self.req_file()
        
        # Plot the attendance for a specific student ID
        self.plot_attendance(self.student_id, excel_file=file_path)

if __name__ == "__main__":
    root = Tk()
    app = Studentinfo(root, student_data)
    root.configure(bg='lightblue')
    root.mainloop()
