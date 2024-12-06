import NotFoundImage from "../../assets/404-not-found-error.jpg";
import InternalServerErrorImage from "../../assets/500-internal-server-error.jpg";
import { ErrorConfig } from "./Errors.types";

export const errorConfig: ErrorConfig = {
  404: {
    image: NotFoundImage,
    title: "404 Not Found",
    caption: "The requested page was not found!",
    showButton: true,
  },
  500: {
    image: InternalServerErrorImage,
    title: "500 Internal Server Error",
    caption:
      "The server encountered and error and couldn't complete your request.",
    showButton: true,
  },
};
