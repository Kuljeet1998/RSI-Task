# Converted csv to xlsx and then performing tasks using xlrd & xlwt
import xlrd, os
import xlwt
import pandas as pd
import openpyxl
from xlutils.copy import copy
# os.rename('Infosys.csv','infosys.xlsx')
rb=xlrd.open_workbook('Infosys.xlsx',encoding_override='utf-8-sig')
wb=copy(rb)
r_sheet=rb.sheet_by_index(0)
w_sheet=wb.get_sheet(0)
avg_gain=0
avg_loss=0
gain=0
loss=0
for row in range(1,r_sheet.nrows):
	op= r_sheet.cell_value(rowx=row, colx=2)
	cl=r_sheet.cell_value(rowx=row, colx=5)
	quantity=r_sheet.cell_value(rowx=row, colx=6)
	diff=round(op-cl,3)
	#print(row,diff)
	w_sheet.write(row,8,diff)
	if(diff<0):
		w_sheet.write(row,9,0)
		w_sheet.write(row,10,abs((diff)))
		if(row<=14):
			loss+=diff
		
	elif(diff>0):
		w_sheet.write(row,10,0)
		w_sheet.write(row,9,(diff))
		if(row<=14):
			gain+=(diff)
	
	if(row==15):
		avg_gain=gain/14
		avg_loss=abs(loss/14)
		w_sheet.write(row,11,round((avg_gain),2))
		w_sheet.write(row,12,round((avg_loss),2))
		rs=abs(avg_gain/avg_loss)
		rsi=round((100-100/(1+rs)),2)
		w_sheet.write(row,13,rsi)
	
	elif(row>15):
		if(diff>0):
			avg_gain=(avg_gain*13+diff)/14
			avg_loss=(avg_loss*13)/14

		elif(diff<0):
			avg_loss=(avg_loss*13-diff)/14
			avg_gain=(avg_gain*13)/14
		
		w_sheet.write(row,11,round(avg_gain,2))
		w_sheet.write(row,12,round(avg_loss,2))
		rs=abs(avg_gain/avg_loss)
		rsi=round((100-100/(1+rs)),2)
		w_sheet.write(row,13,rsi)

wb.save("Infosys.xlsx")