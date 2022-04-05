import { Button } from "primereact/button";
import { GetStyle } from "./UIComponentCommonUtils";

const GetButton = (props: {
  buttonId: string;
  buttonDisplayText: string;
  onChange: (arg0: any) => void;
}) => {
  return (
    <Button
      type="button"
      className="p-button-raised p-button-rounded"
      label={props.buttonDisplayText}
      tooltip="View Configurations"
      tooltipOptions={{ position: "bottom" }}
      style={GetStyle(props.buttonId)}
      onClick={(e) => props.onChange(e)}
    />
  );
};

export default GetButton;
