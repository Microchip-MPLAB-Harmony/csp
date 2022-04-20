import { GetUIComponentWithLabel } from "./UIComponents/UIComponentCommonUtils";

const AddMultipleFields = (props: {
  componentId: any;
  parentUpdate: () => void;
  symbolsArray: string[];
}) => {
  function updateValue() {
    props.parentUpdate();
  }

  function GetComponents() {
    return (
      <div>
        {props.symbolsArray.map((object: string) => (
          <GetUIComponentWithLabel
            componentId={props.componentId}
            symbolId={object}
            symbolListeners={[object]}
            onChange={updateValue}
          />
        ))}
      </div>
    );
  }
  return (
    <div>
      <div>
        <div className="p-fluid">
          <GetComponents />
        </div>
      </div>
    </div>
  );
};
export default AddMultipleFields;
