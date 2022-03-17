import SimpleImageSlider from "react-simple-image-slider";
import image1 from "../backgroundimage/1.png";
import image2 from "../backgroundimage/2.png";
import image3 from "../backgroundimage/3.jpg";
import image4 from "../backgroundimage/4.jpg";

const images = [
  { url: image1 },
  { url: image2 },
  { url: image3 },
  { url: image4 },
];

const App = () => {
  return (
    <div>
      <SimpleImageSlider
        style={{ margin: "0 auto" }}
        width={1920}
        height={600}
        images={images}
        showBullets={true}
        showNavs={true}
        autoPlay={true}
      />
    </div>
  );
};
export default App;
