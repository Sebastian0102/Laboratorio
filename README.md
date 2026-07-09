# SSH Hardening & Audit Automation Tool
 
## Descripción del Proyecto
 
Este proyecto es una herramienta de automatización diseñada para auditar y aplicar configuraciones de seguridad (hardening) en el servicio SSH de servidores basados en Linux (Ubuntu/Debian). Utiliza **Ansible** para gestionar la configuración de forma masiva y segura, reduciendo la superficie de ataque contra accesos no autorizados y ataques de fuerza bruta.
 
---
 
## Requisitos del Software
 
Para ejecutar este playbook de automatización, el nodo de control necesita tener instalado el siguiente software:
 
- **Sistema Operativo:** Linux (Ubuntu 22.04 LTS o superior recomendado) o macOS.
- **Python:** Versión 3.10 o superior.
- **Ansible:** Versión 2.15 o superior.
- **Acceso SSH:** Llaves SSH configuradas previamente con el usuario administrador (`sudo`) en los servidores destino.
---
 
## Instrucciones de Instalación Paso a Paso
 
### 1. Clonar el repositorio
 
Primero, clona este repositorio en tu máquina local o nodo de control de Ansible:
 
```bash
git clone https://github.com/TU_USUARIO/ssh-hardening-automation.git
cd ssh-hardening-automation
```
 
### 2. Instalar Ansible
 
Si no tienes Ansible instalado, ejecuta los siguientes comandos en tu terminal:
 
```bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
```
 
### 3. Configurar el inventario
 
Edita el archivo `inventory.ini` e incluye las direcciones IP o dominios de tus servidores objetivos:
 
```ini
[servers]
192.168.1.50
192.168.1.51
```
 
---
 
## Ejemplo de Uso
 
### Ejecutar la Auditoría y Aplicar los Cambios
 
Para aplicar las políticas de seguridad en los servidores listados en el inventario, ejecuta el comando principal utilizando privilegios de `sudo`:
 
```bash
ansible-playbook -i inventory.ini site.yml --ask-become-pass
```
 
### ¿Qué hace este script de automatización?
 
1. Deshabilita el acceso del usuario `root` a través de SSH.
2. Desactiva la autenticación mediante contraseñas (obliga a usar llaves SSH).
3. Cambia el puerto SSH por defecto (del 22 a un puerto personalizado, ej. 2222).
4. Configura el tiempo de desconexión por inactividad (`ClientAliveInterval`).
5. Reinicia el servicio SSH de manera segura para aplicar los cambios.
---
 
## Captura de Pantalla del Resultado Esperado
 
A continuación se muestra la ejecución exitosa del playbook en la terminal, donde se observa que las tareas se completaron correctamente sin errores (`failed=0`):
 
> **Nota:** Recuerda reemplazar esta imagen de ejemplo por una captura de pantalla real de tu terminal ejecutando un comando de Git o Ansible.
 
---
 
## Licencia
 
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE) adjunto en este repositorio.
