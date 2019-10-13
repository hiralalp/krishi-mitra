import xlrd 
  
loc = ("agri_ques.xlsx") 
conversation=[]
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
#print(sheet.cell_value(0, 0)) 
r=sheet.nrows
c=sheet.ncols
for i in range(0,r):
	for j in range(0,c):
		conversation.append(sheet.cell_value(i,j))
print(conversation)