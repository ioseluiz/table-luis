from paddleocr import PPStructure
import os

def main():
    table_engine = PPStructure(show_log=True, image_orientation=True)
    save_folder = './output'
    imgs_folder = './imgs'
    # Get list of images
    imgs = os.listdir(imgs_folder)
    for img in imgs:
        print(img)
        
        
        img_path = './image/cropped_GUPC-REQ-170+172_00000001_page_1.jpg'
    img = cv2.imread(img_path)
    result = table_engine(img)
    # print(len(result))
    # save_structure_res(result, save_folder,os.path.basename(img_path).split('.')[0])

    for line in result:
        line.pop('img')
        list_header = []
        data = []
        html = line['res']['html']
        soup = BeautifulSoup(html, "html.parser")
        header = soup.find_all("table")[0].find_all("tr")[1]
        # print(header)
        
        for items in header:
            try:
                list_header.append(items.get_text())
            except:
                continue
        print(list_header)
            
        HTML_data = soup.find_all("table")[0].find_all("tr")[2:]
        
        for element in HTML_data:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    continue
            data.append(sub_data)
            
        df = pd.DataFrame(data=data, columns=list_header)
        df_row = df.tail(1)
        df_row.to_csv('table_data.csv')
        
if __name__ == "__main__":
    main()