import { useState } from "preact/hooks";
import ImageUpload from "../../components/ImageUpload";
import Layout from "../../layout";
import combineSwatchandSilhouette from "./api";
import "./newUpload.css";
import ResultModal from "../../components/resultModal";

export interface OurImages {
  swatch: File | null;
  silhouette: File | null;
}

export default function NewUploadPage() {
  const [images, setImages] = useState<OurImages>({
    swatch: null,
    silhouette: null,
  });

  const [ showModal, setShowModal ] = useState(false);
  const [ result, setResult ] = useState('');

  const fetchResult = async () => {
    try {
      const { swatch, silhouette } = images;
      if (!(swatch && silhouette)) {
        throw new Error("either swatch or silhouette or both are not set");
      }
      const res = await combineSwatchandSilhouette(swatch, silhouette);
      setResult(res);
      setShowModal(true);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setResult('');
  }

  return (
    <Layout>
      <section className="newUpload-wrapper">
        {result && showModal && <ResultModal imageUrl={result} handleClose={handleCloseModal}/>}
        <ImageUpload uploadType="swatch" images={images} setImage={setImages} />
        <ImageUpload
          uploadType="silhouette"
          images={images}
          setImage={setImages}
        />
        <button 
          disabled={!(images.silhouette && images.swatch)}
          className="submit-button" onClick={fetchResult}>
          {" "}
          Click to See Result{" "}
        </button>
      </section>
    </Layout>
  );
}
