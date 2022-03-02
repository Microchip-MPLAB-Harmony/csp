import { GetUIComponentWithOutLabel } from './UIComponent';

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
          <GetUIComponentWithOutLabel
            componentId={props.componentId}
            symbolId={object}
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
