import cv2
cap = cv2.VideoCapture("video.mp4")

#tracker_name = cv2.legacy.TrackerCSRT_create
tracker_name = cv2.legacy.TrackerKCF_create

trackers = cv2.legacy.MultiTracker_create()

while True:
    ret,frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(960,540))
        (success, box) = trackers.update(frame)
        for b in box:
            (x,y,w,h) = [int(i) for i in b]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Frame",frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):break
        elif key == ord("t"):
            box1 = cv2.selectROI("frame",frame,fromCenter=False)
            tracker = tracker_name()
            trackers.add(tracker,frame,box1)
    else: break
cap.release()
cv2.destroyAllWindows()