import { Errors } from "../../containers/Errors";

export const NotFound = () => {
  return <Errors status={404} />;
};
