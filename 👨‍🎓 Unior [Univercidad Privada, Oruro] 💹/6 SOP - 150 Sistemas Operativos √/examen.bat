@echo off

title Calculadora
echo Calculadora

set var=0
set num1=0
set num2=0
set resultado=0
set opc=0

:menu
echo.
echo Digite un numero
set /p num1=

echo Digite otro numero
set /p num2=

echo.

:operaciones
echo.
echo 1 Suma
echo 2 Resta
echo 3 Multiplicacion
echo 4 Division
echo 5 Salir

echo.

set /p var=

echo.

if %var%==1 goto :suma
if %var%==2 goto :resta
if %var%==3 goto :multiplicacion
if %var%==4 goto :division
if %var%==5 goto :salir

:suma
set /a resultado=%num1%+%num2%
echo La suma de %num1% y %num2% es: %resultado%
echo.
goto :orden

:resta
set /a resultado=%num1%-%num2%
echo La resta entre %num1% y %num2% es: %resultado%
echo.
goto :orden

:multiplicacion
set /a resultado=%num1%*%num2%
echo La multiplicacion entre %num1% y %num2% es: %resultado%
echo.
goto :orden

:division
set /a resultado=%num1%/%num2%
echo La division entre %num1% y %num2% es: %resultado%
echo.
goto :orden

:limpiar
cls
goto :menu

:orden
echo 1 Hacer otra operacion con los mismos numeros
echo 2 Ingresar otros numeros
echo 3 Limpiar pantalla
echo 4 salir
echo.
set /p opc=

if %opc%==1 goto :operaciones
if %opc%==2 goto :menu
if %opc%==3 goto :limpiar
if %opc%==4 goto :salir

:salir
echo.
echo Gracias por utilizar la calculadora
echo.
pause
exit