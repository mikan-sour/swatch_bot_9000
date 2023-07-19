import { useRef } from "preact/hooks";
import "./resultModal.css";
export default function ResultModal({
  handleClose,
  imageUrl,
}: {
  handleClose: () => void;
  imageUrl: string;
}) {
  const modalImageRef = useRef<HTMLImageElement>(null);

  const handleDownload = () => {
    if (!modalImageRef.current) {
      return;
    }
    const container = modalImageRef.current;
    const { width, height } = container.getBoundingClientRect();

    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');

    canvas.width = width;
    canvas.height = height;

    if(!context) return;
    context.fillStyle = 'white';
    context.fillRect(0, 0, width, height);

    const image = new Image();
    image.src = imageUrl;

    image.onload = () => {
      context?.drawImage(image, 0, 0, width, height);

      const dataURL = canvas.toDataURL('image/png');

      const link = document.createElement('a');
      link.href = dataURL;
      link.download = 'image.png';
      link.click();
    };
  };

  
  return (
    <section className="overlay" onClick={handleClose}>
      <div className="modal-wrapper">
        <img src={imageUrl} ref={modalImageRef}/>
        <div className="modal-actions" >
          <button onClick={handleClose}>close</button>
          <button onClick={handleDownload}>download</button>
        </div>
      </div>
    </section>
  );
}
