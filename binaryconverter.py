from PIL import Image

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

img = Image.open('image.png')
text = tess.image_to_string(img)

# buat ganti character yang salah
def repl(z):
   list2 =[]
   for a in z:
      if a == "7":
        a="1"
        list2.append(a)
      elif a == "O":
         a="0"
         list2.append(a)
      elif a == "T":
         a="1"
      else:
         list2.append(a)
   return "".join(list2)
   

print(text)
source = text.split("\n")
binary_char = []
for x in range(len(source)):
   y = source[x].split(" ")
   for z in y:
      if "7" in z or "O" in z or "T" in "T":
        i = y.index(z)
        up=repl(z)
        z=up
      binary_char.append(z)
print(binary_char)
   
# buat convert binary ke character
def convert(bin):
   list3=[]
   list4=[]
   for num in bin:
      if "0" in num and "1" in num:
         binary_int = int(num, 2)
         byte_number = binary_int.bit_length() + 7 // 8
         binary_array = binary_int.to_bytes(byte_number, "big")
         ascii_text = binary_array.decode()
      else:
         num2=" "+num
         list4.append(num2)
         
      list3.append(ascii_text)
   list5=list3+list4
   print(" ")
   print("terjemahannya adalah: ")
   print(" ")
   print("".join(list5))
         
convert(binary_char)
