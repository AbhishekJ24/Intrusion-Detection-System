import { useNavigate } from "react-router-dom";
import { ErrorProps } from "./Error.types";

export const Error = (props: ErrorProps) => {
  const { image, title, caption, showButton } = props;
  const navigate = useNavigate();

  const handleNavigation = () => {
    void navigate("/");
  };

  return (
    <div className="flex flex-col justify-center items-center gap-8 min-h-[48rem]">
      <div className="h-96 aspect-square">
        <img src={image} alt={title} className="h-full w-full" />
      </div>
      <h1 className="text-6xl font-bold text-center w-1/2">{caption}</h1>
      {showButton && (
        <button
          onClick={handleNavigation}
          className="bg-[#565C70] hover:bg-[#697088] px-6 py-2 rounded-lg"
        >
          Go Home
        </button>
      )}
    </div>
  );
};
