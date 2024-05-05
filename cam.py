import cv2

# Charger le détecteur de visages pré-entraîné
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturer la vidéo en direct à partir de la caméra
cap = cv2.VideoCapture(0)

# Votre nom à afficher sous chaque cadre de visage détecté
votre_nom = "Ismail"

# Boucle pour lire chaque image de la vidéo en direct
while cap.isOpened():
    # Lire l'image de la vidéo
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Détecter les visages dans l'image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Dessiner des rectangles autour des visages détectés et afficher votre nom
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, votre_nom, (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    # Afficher la vidéo en direct avec les rectangles dessinés et votre nom
    cv2.imshow('Video', frame)
    
    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()
