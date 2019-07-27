# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:09:29 2018

@author: Emilio Ferreira
To do
	--- Adicionar identificação de alvo principal
	--- Adicionar complementos de mira interativos
	--- Adicionar IDE(ajuste de limites interativos)
	--- Comunicação serial
Changelog
	V 0.1 - 24/01/2017    Emilio
	--- Adicionado a detecção de movimento 
	--- Adicionado retangulo de alvo  
	--- Centro do retangulo    
"""
import numpy as np
import cv2

AREAMIN = 10000  # Área minima de captura de contorno
camera = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
	ret, frame = camera.read()
	fgmask = fgbg.apply(frame)
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel) #filtra a diferença de movimento?
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations = 2)
	frame2, contorno, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	for i in contorno:
		if cv2.contourArea(i) < AREAMIN:
			continue
		(x, y, w, h) = cv2.boundingRect(i)     # desenha um retangulo verde no alvo
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		#desenha um circulo vermelho exatamente no centro do alvo
		#centro do alvo [round( ( x+w/2) ), round( ( y+h/2) )]
		cv2.circle(frame, (round((x+w/2) ), round((y+h/2) ) ), 3, (0,0,255), -1) 
		

	cv2.imshow('Camera', frame) #mostra imagem da camera 
	cv2.imshow('Mask', fgmask) #mostra a imagem da camera com diferança de movimento


	#fecha a janela caso a letra precionada seja 'q'
	if cv2.waitKey(1) & 0xFF == ord('q'):  
		break
# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
    