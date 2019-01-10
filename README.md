# Hardware
- Raspberry Pi 3 Model B+ or ODROID-XU4 (for YOLO)
- Pixhawk PX4
- Logitech C922 Webcam

# Requirement
- python 2.7
- OpenCV 3 or higher
- Dronekit-python
- pymavlink 1.1.69

# FAQ
## Connection Part
Q : link timeout no heartbeat in last 5 seconds หรืออื่นๆที่เกี่ยวกับการเชื่อมบอร์ด<br/>
    ```
    เช็คเวอร์ชั่น pymavlink และ Dronekit ต้อง clone จาก git เท่านั้น
    ```
## Vision Part
Q : Contours คืออะไร ?<br/>
    ```
    จุดที่ต่อเนื่องกัน ตามแนวที่มีสี/ความเข้ม เดียวกัน
    ```
Q : BGR คืออะไร ?<br/>
    ```
    Color Space ที่นิยมในอุสาหกรรมกล้องและผู้ให้บริการซอฟต์แวร์ คล้ายๆ RGB แค่สลับchannel R, B
    ```
Q : ทำไมต้องแปลง BGR เป็น HSV ?<br/>
    ```
    HSV มีค่าแสง/ค่าความอิ่ม มาเกี่ยวข้องทำให้เหมาะกับการใช้งานกับวัตถุจริงมากกว่า BGR
    ```
Q : ลด noise ยังไง ?<br/>
    ```
    มีหลายวิธี ตั้งแต่การเบลอภาพ, การทำEqualization, การทำMorphological Transformations, ฯลฯ
    ```
Q : AreaRes, xRes, yRes คืออะไร ทำไมต้องทำ ?<br/>
    ```
    ปรับขนาดหน้าจอให้อยู่ในช่วง (-1, -1) ถึง (1, 1) เพื่อเป็นมาตรฐานเดียวกัน<br/>
    ถ้าไม่ทำจะมีปัญหาเวลา resize, เปลี่ยนกล้อง, ฯลฯ 
    ```
Q : แยก Features ยังไงได้บ้าง ?<br/>
    ```
    ใช้สี, ขนาด, รูปทรง, ความกว้าง-ยาว, อัตราส่วนความกว้างค่อความยาว, ฯลฯ
    ```