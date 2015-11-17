'''
Created on 2015. 10. 24.

@author: SUNgHOOn
트레이닝셋에 리콜타입 머지
old_rcl_out_14.txt 파일을 읽어
software.txt
hardware.txt
etc.txt
의 ID와 비교하여 
new_rcl_out_14.txt 파일 생성
'''

# recall_2014_file = open("../old_rcl_out_14.txt", "r", encoding='utf8')
# recall_2014_outfile = open("../new_rcl_out_14.txt", "w", encoding='utf8')

recall_2014_file = open("../FLAT_RCL_Out_15_new.txt", "r", encoding='utf8')
recall_2014_outfile = open("../new_rcl_out_15.txt", "w", encoding='utf8')
for line in recall_2014_file:
    line = line.strip()
    rcl_id = line[0:9]
    
    #print(rcl_id)
    
    search_id = ""
#     sw_file = open("../software.txt", "r")
    sw_file = open("../software2015.txt", "r")
    for sw_id in sw_file:
        sw_id = sw_id.strip()
        if rcl_id == sw_id:
            search_id = sw_id
            line = "SWT " + line
            recall_2014_outfile.write(line)
            recall_2014_outfile.write("\n")
            break
        
#     if search_id == "":
#         hw_file = open("../hardware.txt", "r")
#         for hw_id in hw_file:
#             hw_id = hw_id.strip()
#             if rcl_id == hw_id:
#                 search_id = hw_id
#                 line = "HWT " + line
#                 break
#              
#     if search_id == "":
#         hw_file = open("../etc.txt", "r")
#         for hw_id in hw_file:
#             hw_id = hw_id.strip()
#             if rcl_id == hw_id:
#                 search_id = hw_id
#                 line = "ETC " + line
#                 break
    
    if search_id == "":
        line = "N " + line
    
#     recall_2014_outfile.write(line)
#     recall_2014_outfile.write("\n")
    print (line)
    
recall_2014_outfile.close()
    