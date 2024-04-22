/* call the function to pass the url of the icon (local) and then the link */
import "./Media.css";

function Media({ icon, url }) {
  return (
    <>
      <a href={url}>
        <img className="sm" src={icon} alt=""></img>
      </a>
    </>
  );
}

export default Media;



