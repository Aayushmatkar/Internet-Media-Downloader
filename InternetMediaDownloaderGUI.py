
from __future__ import unicode_literals
import os
import requests # to sent GET requests
from bs4 import BeautifulSoup # to parse HTML
from tkinter import *
import tkinter as tk
import traceback
from tkinter import messagebox as m_box
from tkinter import filedialog
from PIL import Image
import youtube_dl
from PIL import ImageTk

root = Tk()
root.title("Media Downloader")



   
yahoo_img = \
    'https://in.images.search.yahoo.com/search/images;_ylt=AwrwJSJD2Q1fTlkATCK8HAx.;_ylc=X1MDMjExNDcyMzAwNARfcgMyBGZyAwRncHJpZAN6VDFjeUl0WlFfLnRqMGU1YlNTTGVBBG5fc3VnZwMxMARvcmlnaW4DaW4uaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDNARxdWVyeQNkb2dzBHRfc3RtcAMxNTk0NzQzMTEw?fr2=sb-top-in.images.search&'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
save_folder = 'images'

#---------------------------------------------------------------------------------
def download_n():
   
    f1=Frame(root)
    z = Canvas(f1, width=400,height=250,bg = "lightgreen")
    image = ImageTk.PhotoImage(file = "E:\\program files\\framsmediadownloader\\sm1.jpg")
    z.create_image(1, 1, image = image, anchor = NW)
           
           
    Label(f1, text="What are you looking for?", fg = "Black",
font = "Verdana 10",bg = "LightGrey").place(x=90,y=20)

    e1=Entry(f1)
    e1.place(x=90,y=50)
   
    Label(f1, text="How many images do you want? ", fg = "Black",
font = "Verdana 10",bg = "LightGrey").place(x=90,y=90)
   
    e2=Entry(f1)
    e2.place(x=90,y=120)
           
    button4 = tk.Button(f1, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:download_images(e1,e2))
    button4.place(x=90,y=160)

   
   
    button5 = tk.Button(f1, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f1.destroy(),main()]).place(x=225,y=160)
       
    z.pack()
    f1.pack()
   
   
   
   
         
       
       
def download_images(e1,e2):
    try:
#        f1=Frame(root)
        data=e1.get()
        n_images=e2.get()
        if data=='' or n_images=='':
#            root1.withdraw()
            m_box.showerror('Error','Please fill both entries ')
        else:
            data=str(data)
            n_images=int(n_images)
        #    print(data,n_images)

#            z = Canvas(f1, width=260,height=110)
           
       
           
            print('Start searching...')
           
       
                   
            # get url query string
            searchurl = yahoo_img + 'p=' + data
                    #print(searchurl)
               
                    # request url, without user_agent the permission gets denied
            response = requests.get(searchurl, headers=user_agent)
            html = response.text
           
            soup = BeautifulSoup(html, 'html.parser')
            results = soup.find_all('img',class_= 'process',limit=n_images)
               
                    # extract the link from the img tag
            imagelinks= []
                   
            for re in results:
                url1=re.attrs.get('data-src')
                imagelinks.append(url1)
           
            print(f'found {len(imagelinks)} images')
#            Label(f1, text=f'found {len(imagelinks)} images', fg = "Black",
#        font = "Verdana 10",bg = "LightGrey").place(x=70,y=20)
            print('Start downloading...')
        #    Label(root1, text="Start downloading...", fg = "Black",
        # font = "Verdana 10").pack()
               
            for i, imagelink in enumerate(imagelinks):
                # open image link and save as file
                response = requests.get(imagelink)
                       
                imagename = save_folder + '/' + data + str(i+1) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
               
            print('Done')
#            Label(f1, text="DOWNLOADING COMPLETE", fg = "Black",
#        font = "Verdana 10",bg = "LightGrey").place(x=40,y=40)
#            button5 = tk.Button(f1, text='OK', width=10,
#                                bg="#D3D3D3",fg='black',
#                                command=f1.destroy).place(x=90,y=70)
            m_box.showinfo(title='Done', message=f'found {len(imagelinks)} images \nDownloading Complete')  
#            z.pack()
           
    except ValueError:
#        root1.withdraw()
        m_box.showwarning('Error','Enter a Valid Number')
#        print("enter valid number")
#        root2 = Tk()
#        z = Canvas(root2, width=260,height=110)
#        Label(root2, text="Enter a valid Number", fg = "Black",
# font = "Verdana 10").place(x=60,y=30)
#        button5 = tk.Button(root2, text='OK', width=10,
#                        bg="#D3D3D3",fg='black',
#                        command=root2.destroy).place(x=90,y=70)
#        
#        z.pack()
#------------------------------------------------------------------------------------


def url_n():
    f2=Frame(root)
    z = Canvas(f2, width=400,height=250,bg = "darkblue")
#    image = ImageTk.PhotoImage(file = "E:/sem4/apsit skills/page1.jpg")
#    z.create_image(1, 1, image = image, anchor = NW)
    Label(f2, text="Enter Url : ", fg = "Black",
font = "Verdana 10",bg = "LightGrey").place(x=90,y=20)

    e1=Entry(f2,width=35)
    e1.place(x=90,y=50)
   
    Label(f2, text="Name of the image to be saved :", fg = "Black",
font = "Verdana 10",bg = "LightGrey").place(x=90,y=90)
   
    e2=Entry(f2)
    e2.place(x=90,y=120)
           
   
    button4 = tk.Button(f2, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:url_images(e1,e2)).place(x=90,y=160)
    button5 = tk.Button(f2, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f2.destroy(),main()]).place(x=225,y=160)
       
       
    z.pack()
    f2.pack()
   
def url_images(e1,e2):
    try:
   
#        root1 = Tk()
#        root1.title("Done")
#
#        z = Canvas(root1, width=260,height=110)
       
        imagelink=e1.get()
        data=e2.get()
        if imagelink=='' or data=='':
#            root1.withdraw()
            m_box.showerror('Error','Please fill both entries ')
        else:
            response = requests.get(imagelink)
            imagename = save_folder + '/' + data +  '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)
            print('Done')
            m_box.showinfo(title='Done', message='Downloading Complete')  
#            Label(root1, text="IMAGE DOWNLOADED", fg = "Black",
#        font = "Verdana 10",bg = "LightGrey").place(x=60,y=30)
#            button5 = tk.Button(root1, text='OK', width=10,
#                                bg="#D3D3D3",fg='black',
#                                command=root1.destroy).place(x=90,y=70)
               
#            z.pack()
    except :
#        root1.withdraw()
        m_box.showwarning('Invalid Url','Enter a Valid URL')
   
       
       
#------------------------------------------------------------------------------------------
   
def insta_n():
    f3=Frame(root)
   
    z = Canvas(f3, width=400,height=250,bg = "darkcyan")
    image = ImageTk.PhotoImage(file = "E:\\program files\\framsmediadownloader\\ig.png")
    z.create_image(1, 1, image = image, anchor = NW)
    Label(f3, text="Enter Instagram Image link : ", fg = "Black",
font = "Verdana 10",bg = "LightGrey").place(x=90,y=20)

    e1=Entry(f3,width=35)
    e1.place(x=90,y=50)
   
    Label(f3, text="Name of the image to be saved :", fg = "Black",
font = "Verdana 10",bg = "LightGrey").place(x=90,y=90)
   
    e2=Entry(f3)
    e2.place(x=90,y=120)
           
    button4 = tk.Button(f3, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:insta_images(e1,e2)).place(x=90,y=160)
    button5 = tk.Button(f3, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f3.destroy(),main()]).place(x=225,y=160)
       
    z.pack()
    f3.pack()
def insta_images(e1,e2):
    try:
     
        url=e1.get()
        data=e2.get()
       
        if data=='' or url=='':

            m_box.showerror('Error','Please fill both entries ')
        else:
            usr_agent = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',}
            response = requests.get(url, headers=usr_agent)
            html = response.text
            #soup = BeautifulSoup(html, 'html.parser')
       
            soup = BeautifulSoup(html,'html.parser')
            metaTag = soup.find_all('meta', {'property':'og:image'})
            imagelink = metaTag[0]['content']
            print(imagelink)
           #=============================================
            #f=filedialog.askdirectory(initialdir='C:/')
            #os.chdir(f)
           #=============================================
            response = requests.get(imagelink)
            imagename = save_folder + '/' + data +  '.jpg'
            with open(imagename, 'wb') as file:
             file.write(response.content)
            print('Done')
            m_box.showinfo(title='Done', message='Downloading Complete')  
           
           
#            Label(root1, text="IMAGE DOWNLOADED", fg = "Black",
#        font = "Verdana 10",bg = "LightGrey").place(x=60,y=30)
#            button5 = tk.Button(root1, text='OK', width=10,
#                                bg="#D3D3D3",fg='black',
#                                command=root1.destroy).place(x=90,y=70)
               
         

    except :
#        root1.withdraw()
        m_box.showwarning('Invalid Instagram Link','Enter a Valid URL')
#        print("Invalid Image Url")
#        root2 = Tk()
#        z = Canvas(root2, width=260,height=110)
#        Label(root2, text="Invalid Image Url", fg = "Black",
# font = "Verdana 10").place(x=60,y=30)
#        button5 = tk.Button(root2, text='OK', width=10,
#                        bg="#D3D3D3",fg='black',
#                        command=root2.destroy).place(x=90,y=70)
#        
#        z.pack()
       
#------------------------------------------------------------------------
def yt_n():
    f4=Frame(root)

    z = Canvas(f4, width=400,height=280,bg="red")
    image = ImageTk.PhotoImage(file = "E:\\program files\\framsmediadownloader\\bgtest3.jpg")
    z.create_image(2, 2, image = image, anchor = NW)
   
    Label(f4, text="Enter Url : ", fg = "Black",
font = "Verdana 10",bg = "LightGrey").place(x=90,y=50)

    e1=Entry(f4,width=35)
    e1.place(x=90,y=80)
   
#    Label(root1, text="Name of the image to be saved :", fg = "Black",
# font = "Verdana 10").place(x=90,y=90)
#    
#    e2=Entry(root1)
#    e2.place(x=90,y=120)
           
   
    button4 = tk.Button(f4, text='Download', width=17,
                        bg="#D3D3D3",fg='black',
                        command=lambda:yt_videos(e1)).place(x=90,y=160)
    button5 = tk.Button(f4, text='Back', width=10,
                        bg="#D3D3D3",fg='black',
                        command=lambda:[f4.destroy(),main()]).place(x=225,y=160)
       
       
    z.pack()
    f4.pack()
   
def yt_videos(e1):
    try:
   
        url=e1.get()
        if url=='' :
       
            m_box.showerror('Error','Please enter url ')
        else:
            ydl_opts = {}
#            root1.withdraw()
            f=filedialog.askdirectory(initialdir='C:/')
            os.chdir(f)
           
           
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            m_box.showinfo(title='Done', message='Downloading Complete')
#            Label(root1, text="VIDEO DOWNLOADED", fg = "Black",
#        font = "Verdana 10",bg = "LightGrey").place(x=60,y=30)
#            button5 = tk.Button(root1, text='OK', width=10,
#                                bg="#D3D3D3",fg='black',
#                                command=root1.destroy).place(x=90,y=70)
#            z.pack()
    except:
#        root1.withdraw()
        m_box.showwarning('Invalid Youtube Link','Enter a Valid URL')
       
       
#-----------------------------------------------------------------------------------------  
   
       


def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
       
    f=Frame(root)
   
   
    w = Canvas(f, width=400,height=280,bg = "black")
   
   
#    root.wm_attributes('-transparentcolor','black')
    image = ImageTk.PhotoImage(file = "E:\\program files\\framsmediadownloader\\sm1.jpg")
    w.create_image(2, 2, image = image, anchor = NW)

#    background_image=tk.PhotoImage(file="E:/sem4/apsit skills/page1.jpg")
#    background_label = Label(root, image=background_image)
#    bakcground_label.pack()
   
#    Label(root, text="Media Downloader", fg = "Black",
#font = "Verdana 14",pady=10,padx=10,bg = "LightGrey").place(x=100,y=20)
   
#    Label(root, text="Media Downloader", fg = "White",bg='black',padx=10,pady=10,
#font = "Verdana 14").place(x=100,y=20)
   
    w.create_text(200,50, text="Media Downloader", fill = "White",font = "Verdana 16")
   
    button1 = tk.Button(f, text='Download n required images', width=35,
                        command=lambda: [download_n(),f.destroy()]).place(x=75,y=100)
    button2 = tk.Button(f, text='Download via url', width=35,
                        command=lambda: [url_n(),f.destroy()]).place(x=75,y=140)
    button3 = tk.Button(f, text='Download instagram images', width=35,
                        command=lambda: [insta_n(),f.destroy()]).place(x=75,y=180)
   
    button4 = tk.Button(f, text='Download youtube videos', width=35,
                       command=lambda: [yt_n(),f.destroy()]).place(x=75,y=220)
 
    w.pack()
    f.pack()
    mainloop()
   
   
   
   
   
   
   
   
if __name__ == '__main__':
    main()
