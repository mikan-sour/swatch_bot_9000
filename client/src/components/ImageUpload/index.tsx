// ImageUpload.tsx

import { FunctionComponent, JSX } from 'preact';
import { StateUpdater } from 'preact/hooks';

import './ImageUpload.css';
import { OurImages } from '../../pages/newUpload';

interface ImageUploadProps {
  uploadType: 'silhouette'|'swatch';
  images:OurImages
  setImage: StateUpdater<OurImages>
}

const ImageUpload: FunctionComponent<ImageUploadProps> = ({ uploadType,images, setImage }) => {

  const handleFileInput = (event: JSX.TargetedEvent<HTMLInputElement, Event>) => {
    const file = event.currentTarget.files && event.currentTarget.files[0];
    if (file && isImageFile(file)) {
      setImage({...images, [uploadType]:file});
    } else {
      // Handle invalid file type
    }
  };

  const handleRemoveFile = () => {
    setImage({...images, [uploadType]:null});
  };

  const isImageFile = (file: File) => {
    return file.type.startsWith('image/');
  };

  

  return (
    <div className={`image-upload ${images[uploadType] ? 'has-image' : ''}`}>
      
      {images[uploadType] ? (
        <div className="image-preview">
          <img src={URL.createObjectURL(images[uploadType] as Blob)} alt="Uploaded File" />
          <button className="remove-file" onClick={handleRemoveFile}>
            &#x2715;
          </button>
        </div>
      ) : 
      <label htmlFor="file-input" className="upload-container">
        <div className="upload-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M0 0h24v24H0z" fill="none" />
            <path
              fill="currentColor"
              d="M14 3H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9l-6-6zm0 2l5 5h-5V5zm-4 11h2v2h-2v-2zm4 0h2v2h-2v-2zm-4 4h2v2H6v-2zm4 0h2v2h-2v-2zm4 0h2v2h-2v-2z"
            />
          </svg>
        </div>
        <div className="upload-text">
          <span>Click to upload a </span><br/><b style={{fontSize:'1.4rem'}}>{uploadType}</b>
        </div>
        <input
            style={{display:'none'}}
          id="file-input"
          type="file"
          accept="image/*"
          onChange={handleFileInput}
        />
      </label>}
    </div>
  );
};

export default ImageUpload;
