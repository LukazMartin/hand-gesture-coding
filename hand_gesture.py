import cv2
import mediapipe as mp
import pyautogui
import math
import pyperclip
from write_code import Write

# Initialize Mediapipe Hand Detection
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize the writing class
write = Write()

#track writing operation
action = None

# Initialize PyAutoGUI for mouse control
pyautogui.FAILSAFE = False

# Open Video Capture Device
cap = cv2.VideoCapture(0)

cv2.waitKey(1)


# Loop over video feed
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        # Read a frame from the video feed
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Convert image to RGB for Mediapipe processing
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Run hand detection
        results = hands.process(image)

        # Draw hand landmarks on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get x, y coordinates of index finger
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

                # Get the x, y, z coordinates of the thumb tip
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Get the x, y, z coordinates of middle finger
                middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

                # Get the x, y, z coordinates of pinky
                pinky_finger = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                distance_i_t = math.sqrt((thumb_tip.x - index_finger.x)**2 + (thumb_tip.y - index_finger.y)**2 + (thumb_tip.z - index_finger.z)**2)
                distance_i_m = math.sqrt((middle_finger.x - index_finger.x)**2 + (middle_finger.y - index_finger.y)**2 + (middle_finger.z - index_finger.z)**2)
                distance_m_p = math.sqrt((middle_finger.x - pinky_finger.x)**2 + (middle_finger.y - pinky_finger.y)**2 + (middle_finger.z - pinky_finger.z)**2)

                if action is None:
                    if middle_finger.y > index_finger_mcp.y and thumb_tip.y + 0.2 > index_finger.y:
                        action = "var"
                        print("One")
                    elif distance_i_m < 0.1 and thumb_tip.y > index_finger_mcp.y and pinky_finger.y > index_finger_mcp.y:
                        action = "func"
                        print("Two")
                    elif distance_i_t < 0.05:
                        action = "spec"
                        print("Ok")
                    elif thumb_tip.y < index_finger.y:
                        action = "send"
                        print("Send")
                    
                    if action is not None:
                        pyperclip.copy("#")
                        pyautogui.hotkey("ctrl", "v")
                        pyautogui.write(f" {action}\n")
                else:
                    if distance_i_t < 0.05:
                        print(f"x: {index_finger.x} y: {index_finger.y}")
                        write.write(index_finger.x,index_finger.y,action)
                        action = None


        # Display the resulting image
        cv2.imshow('Hand Gesture Recognition', image)

        # Exit the program on pressing 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release Video Capture Device
cap.release()

# Close all windows
cv2.destroyAllWindows()
