#! /usr/bin/bash

NOM=uno

DIR_WRK=$PWD

DIR_LOG=$DIR_WRK/log
FIC_LOG=$DIR_LOG/$(basename $0 .sh).$NOM.log # $0 segurament tingui el path complet, basename de $0 per treure el pathcomplet i .sh per el final si coincideix en aquest cas treu l'extensió
[ -d $DIR_LOG ] || mkdir -p $DIR_LOG  # Errno.h estandar de codigs d'error 0 igual a success, -d dirlog mira si existeix el directori, si el troba ja no executa la resta del or, es un curt circuit. Si la primera condició es falça executara la resta de la lina logica

exec > >(tee $FIC_LOG) 2>&1
# el tee es una T, llegeix del teclat o fitxer escriu per pantalla i ademes ho desvia a un fitxer. El 2>&1 desvia la sortida d'error a la sortida estandard.
# exec el que fa es executar la linea de comandes que li passis sense crear un nou proces. El primer > redirecciona la sortida estandar a un fitxer i el segon > fa creure a el sistema que el que bé després es un fitxer, el tree guardara tot al fitxer mentre podras seguir veient el teu output per pantalla i el 2>&1 redirigira també els errors a el log. Si possesis pipeline estaries creant 2 procesos

hostname
pwd 
date 
echo "Nom del fitxer de log: $FIC_LOG"
echo "inici del script $0"

PRM=true
ENT=true
REC=true
EVA=true

DIR_GUI=$DIR_WRK/Gui
GUI_ENT=$DIR_GUI/train.gui
GUI_DEV=$DIR_GUI/devel.gui

DIR_SEN=$DIR_WRK/Sen
DIR_PRM=$DIR_WRK/Prm/$NOM
DIR_REC=$DIR_WRK/Rec/$Nom
FIC_MOD=

LIS_MOD=$DIR_WRK/Lis/vocales.lis

FIC_RES=$DIR_WRK/Res/$NOM.res
[ -d $(dirname $FIC_RES) ] || mkdir -p $(dirname $FIC_RES)

EXEC="parametriza.py -p $DIR_PRM -s $DIR_SEN $GUI_ENT $GUI_DEV"
$PRM && echo $EXEC && $EXEC || exit 1 # && executa la seguent comanda si la primera es true, echo sempre es true per tant si $PRM es true s'executara tot i si $EXEC dona un error fara exit 1






