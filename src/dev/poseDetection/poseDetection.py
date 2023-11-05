import mediapipe as mp
import cv2

#poseDetection will take a frame as an input
#and return the x & y coordinates of the person's wrist
#input: frame
#output: [(x,y), (x,y)]

def poseDetection(frame):
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # Perform pose estimation
    results = pose.process(rgb_frame)

    # Extract landmarks if pose detected
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        # You can access the landmarks like landmarks[mp_pose.PoseLandmark.WRIST_RIGHT.value]
        # or any other specific landmark.

        # Right wrist landmark (index is 16)
        right_wrist_x = int(landmarks[16].x * frame.shape[1])
        right_wrist_y = int(landmarks[16].y * frame.shape[0])

        # Left wrist landmark (index is 15)
        left_wrist_x = int(landmarks[15].x * frame.shape[1])
        left_wrist_y = int(landmarks[15].y * frame.shape[0])
    
        return [(right_wrist_x, right_wrist_y), (left_wrist_x, left_wrist_y)]


if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the BGR image to RGB 
        results = poseDetection(frame)
        print(results)
        if results:
            (right_wrist_x, right_wrist_y), (left_wrist_x, left_wrist_y) = results[0], results[1]

            #Draw circles at wrist landmarks
            cv2.circle(frame, (right_wrist_x, right_wrist_y), 15, (0, 0, 255), -1)
            cv2.circle(frame, (left_wrist_x, left_wrist_y), 15, (0, 0, 255), -1)
            

        # Draw the pose landmarks on the frame if needed
        # (you can customize this part for your game)
        # e.g., cv2.circle(frame, (landmark_x, landmark_y), 5, (0, 0, 255), -1)
            cv2.imshow('Pose Estimation', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Exit when the user presses the 'Esc' key
            break

    cap.release()
    cv2.destroyAllWindows()
