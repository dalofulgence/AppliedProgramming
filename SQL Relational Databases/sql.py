from tabulate import tabulate
import mysql.connector

print()
print("WELCOME TO THE MySQL HOSPITAL DATABASE")
print("PLEASE CHOOSE A  NUMBER OPTION")
print()


# Prompt the user to chose options

choice = None
while choice != "8":
  print("1) Show Tables Name")
  print("2) Show Table Content")
  print("3) Insert Into Table")
  print("4) Delete Row From Table")
  print("5) Drop Table")
  print("6) Update Table")
  print("8) Quit")
  print()

  choice = input("Please choose number and press enter: ")
  print()

  if choice == "1":
    # Connect to MySql database
    mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")

    mycursor = mydb.cursor()
    # show tables in hospital database.
    mycursor.execute("SHOW TABLES FROM HOSPITAL")
    headers = ["Table Name"]
    print(tabulate(list(mycursor), headers, tablefmt="grid"))
    for x in mycursor.fetchall():
      print(x)
      print()

      # TABLE CONTENT
  elif  choice == "2":
    sub_choice = None
    while sub_choice != "quit":
      sub_choice = input("Enter Table Name :'billing; department; doctor; patient; doctor_department' and type quit to exit: ")

      # billing content
      if sub_choice == "billing":
        mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM billing")
        headers = ["Billing ID", "Patient Name"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print()   

          # department content
      elif sub_choice == "department":
          mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM department")
          headers = ["Department ID", "Department Name"]
          print(tabulate(list(mycursor), headers, tablefmt="grid"))
          for x in mycursor.fetchall():
            print(x)
            print()

            # patient content
      elif sub_choice == "patient":
          mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM patient")
          headers = ["Patient ID", "First Name", "Last Name", "Address", "Phone", "DOB", "Doctor ID", "Billing ID"]
          print(tabulate(list(mycursor), headers, tablefmt="grid"))
          for x in mycursor.fetchall():
            print(x)
            print() 

            # doctor content
      elif sub_choice == "doctor":
          mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM doctor")
          headers = ["Doctor ID", "First Name", "Last Name", "Department Name", "DOB", "Phone"]
          print(tabulate(list(mycursor), headers, tablefmt="grid"))
          for x in mycursor.fetchall():
            print(x)
            print() 

            # doctor deprtment content
      elif sub_choice == "doctor_department":
          mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM doctor_department")
          headers = ["Doctor ID", "Department ID"]
          print(tabulate(list(mycursor), headers, tablefmt="grid"))
          for x in mycursor.fetchall():
            print(x)
            print()

            #  INSERT
  elif choice == '3':
    mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
    mycursor = mydb.cursor()
    table_name = input('Which table to insert into? ')

  # insert into billing 
    if table_name == 'billing':
      billing_id = input('Billing ID: ')
      patient = input('Patient Name: ')
      values = (billing_id, patient)
      sql = "INSERT INTO billing (idbilling, patient_name) VALUES (%s, %s)"
      values = (billing_id, patient)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

      # inserting in department table
    elif  table_name == 'department':
      department_id = input('Department ID: ')
      department = input('Department Name: ')
      values = (department_id, department)
      sql = "INSERT INTO department (iddepartment, department_name) VALUES (%s, %s)"
      values = (department_id, department)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

      # inserting in doctor table
    elif  table_name == 'doctor':
      doctor_id = input('Doctor ID: ')
      f_name = input('First Name: ')
      l_name = input('Last Name: ')
      department = input('Department Name: ')
      dob = input('Date Of Birth (yyyy-mm-dd): ')
      phone = input('Phone Number (000-000-0000): ')
      values = (doctor_id, f_name, l_name, department, dob, phone)
      sql = "INSERT INTO department (iddoctor, first_name, last_name, department_name, date_of_birth, phone) VALUES (%s, %s, %s, %s, %s, %s)"
      values = (doctor_id, f_name, l_name, department, dob, phone)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

      # inserting in patient table
    elif  table_name == 'patient':
      patient_id = input('Patient ID: ')
      f_name = input('First Name: ')
      l_name = input('Last Name: ')
      address = input('Address: ')
      phone = input('Phone Number (000-000-0000): ')
      dob = input('Date Of Birth: (yyy-MM-DD: ')
      doctor_id = input('Doctor ID: ')
      billing_id = input('Billing ID: ')
      values = (patient_id, f_name, l_name, address, phone, dob, doctor_id, billing_id)
      sql = "INSERT INTO patient (idpatient, first_name, last_name, address, phone,  date_of_birth, doctor_iddoctor, billing_idbilling) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      values = (patient_id, f_name, l_name, address, phone, dob, doctor_id, billing_id)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.") 
      print()   

      # inserting in doctor department table
    elif  table_name == 'doctor_department':
      doctor_id = input('Doctor ID: ')
      department_id = input('Department ID: ')
      values = (doctor_id, department_id)
      sql = "INSERT INTO department (doctor_iddoctor, department_iddepartment) VALUES (%s, %s)"
      values = (doctor_id, department_id)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

      # DELETE Row 
  elif choice == "4":
    mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
    mycursor = mydb.cursor()
    table_delete = input('Which table to delete From? ')

    # deleting in billing table
    if table_delete == 'billing':
      bil = input('Billing ID: ')
      sql = f"DELETE FROM billing WHERE idbilling = {bil}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()

      # deleting in department table
    elif table_delete == 'department':
      dep = input('Department ID: ')
      sql = f"DELETE FROM department WHERE iddepartment = {dep}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()

      # deleting in doctor table
    elif table_delete == 'doctor':
      doc = input('Doctor ID: ')
      sql = f"DELETE FROM doctor WHERE iddoctor = {doc}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()

      # deleting in patient table
    elif table_delete == 'patient':
      pat = input('Patient ID: ')
      sql = f"DELETE FROM patient WHERE idpatient = {pat}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()   

      # deleting in doctor department table
    elif table_delete == 'doctor_department':
      doc_dep = input('DOCTOR DEPARTMENT ID: ')
      sql = f"DELETE FROM doctor_department WHERE doctor_iddoctor = {doc_dep}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()

      # Drop table
  elif choice == "5":
    mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
    mycursor = mydb.cursor()
    table_drop = input('Which table to drop? Please consult Table Names: ')
    sql = f"DROP TABLE {table_drop}"
    mycursor.execute(sql)
    print(f"{table_drop} Droped")
    print()

    # Update Table
  elif choice == "6":
    mydb = mysql.connector.connect(host="localhost",user="root",password="Gatouso84@",database="hospital")
    mycursor = mydb.cursor()
    # prompt the user for info to update
    table_update = input('Which table to update from? ')
    column_update = input('which column to update? ')
    value_update = input('New Value(s): ')
    old_value = input('Old value(s): ')
    # run the query
    sql = f"UPDATE {table_update} SET {column_update} = '{value_update}' WHERE {column_update} = '{old_value}'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    print()
    



      


    




    



                
    

 




