from bs4 import BeautifulSoup  #importing the beautiful soup library
import requests, openpyxl


excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Report'
print(excel.sheetnames)


# creating an try and except block for identification of error in source link

try:
    source = requests.get('https://www.ourcommons.ca/Members/en/search')
    source.raise_for_status()    #if the source address is not working

    soup = BeautifulSoup(source.text, 'html.parser') #for receiving the html content of the source page  
    
    members = soup.find('div', id="mip-tile-view").find_all('div')

    for member in members:
        try:
            name = member.find('div', class_="ce-mip-mp-tile-container")
            
            id = name.get("id").split("-")[-1]

            fname = name.find('div', class_="ce-mip-mp-name").text

            party = name.find('div', class_="ce-mip-mp-party").text

            consistuency = name.find('div', class_="ce-mip-mp-constituency").text

            province = name.find('div',class_="ce-mip-mp-province").text

            # image = "https://www.ourcommons.ca" + name.find('div',class_="ce-mip-mp-picture-container").find('img').get('src')

            imgurl ="https://www.ourcommons.ca" + name.find('div',class_="ce-mip-mp-picture-container").find('img').get('src')
            # print(imgurl

            memberurl ="https://www.ourcommons.ca" + name.find('div',class_="ce-mip-mp-tile-container").find('a').get('src')
            print(memberurl)

            print(id, fname, party, consistuency, province, imgurl)
            sheet.append([id, fname, party, consistuency, province, imgurl])
            print("appended")

        except Exception as e:
            continue
    
except Exception as e:
    print(e)


excel.save('report.xlsx')
excel.close()