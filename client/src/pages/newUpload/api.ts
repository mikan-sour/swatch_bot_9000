// const apiHost = process.env.REACT_APP_API_HOST;
// const apiPort = process.env.REACT_APP_API_PORT;
export default async function combineSwatchandSilhouette(swatchFile:File, silhouetteFile:File) {
    const formData = new FormData();
    formData.append('swatch', swatchFile);
    formData.append('silhouette', silhouetteFile);
  
    try {
      const response = await fetch(`http://localhost:8080/thing`, {
        method: 'POST',
        body: formData
      });
  
      if (!response.ok) {
        throw new Error('Upload failed');
      }
  
      const blob = await response.blob();
      return URL.createObjectURL(blob)
    } catch (error) {
      console.error('Error uploading files:', error);
      throw error;
    }
  }