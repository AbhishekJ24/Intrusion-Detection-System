import { Errors } from "../../containers/Errors";

export const InternalServerError = () => {
  return <Errors status={500} />;
};
