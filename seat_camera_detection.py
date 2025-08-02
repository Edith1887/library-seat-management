import cv2, time, os, sys, django
sys.path.append("D:/library-seat-management")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "libraryapp.settings")
django.setup()

from seatmanager.models import Seat
seat = Seat.objects.get(seat_id="A1")

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

last_seen = time.time()
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) > 0:
        seat.status = 'red'
        seat.save()
        last_seen = time.time()
    elif time.time() - last_seen > 10:
        seat.status = 'green'
        seat.save()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()