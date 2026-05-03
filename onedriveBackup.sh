rsync -av --delete /home/rouse/Documents/ /home/rouse/OneDrive/Linux_Documents/

echo "***"
echo "Fase 1:Sincronização da pasta ~/Documents para a pasta OneDrive do Linux"
echo "***"

onedrive --sync --upload-only --single-directory "Linux_Documents" 
echo "***"
echo "Fase 2: Sincronização para a nuvem feita."
echo "***"