import { Error } from "../../components/Error";
import { errorConfig } from "./Errors.config";
import { ErrorsProps } from "./Errors.types";

export const Errors = (props: ErrorsProps) => {
  const { status } = props;
  const error = errorConfig[status];

  return <Error {...error} />;
};
