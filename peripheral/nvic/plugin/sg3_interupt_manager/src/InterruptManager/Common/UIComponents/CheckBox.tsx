import { Checkbox } from "primereact/checkbox";
import React from "react";
import {
  AddSymbolListner,
  UpdateSymbolValue,
} from "../SymbolAccess";
import { convertToBoolean } from "../Utils";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListners: any;
  symbolValue: string;
  styleObject: any;
  editable: boolean;
  visible: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  checkBoxstatus?: any;
  checkBoxEditableState?: boolean;
  checkBoxVisibleState?: boolean;
}
let obj: GetCheckBox | null = null;

class GetCheckBox extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      checkBoxstatus: convertToBoolean(this.props.symbolValue),
      checkBoxEditableState: this.props.editable,
      checkBoxVisibleState: this.props.visible,
    };
    obj = this;
    this.props.symbolListners.forEach(this.Addlistner);
  }

  Addlistner(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListner(value);
  }

  updateValue(checked: boolean) {
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, checked);
    this.props.onChange(checked);
    this.changeValue(checked);
  }

  changeValue(checked: any) {
    this.setState({
      checkBoxstatus: convertToBoolean(checked),
    });
  }

  changeEditableStatus(value: any) {
    this.setState({
      checkBoxEditableState: value,
    });
  }

  changeComponentState(value: any, editable: boolean, visible: boolean) {
    this.setState({
      checkBoxstatus: convertToBoolean(value),
      checkBoxEditableState: editable,
      checkBoxVisibleState: visible,
    });
  }

  render() {
    return (
      <div>
        {this.state.checkBoxVisibleState && (
          <Checkbox
            id={this.props.symbolId}
            inputId="binary"
            style={this.props.styleObject}
            checked={this.state.checkBoxstatus}
            disabled={!this.state.checkBoxEditableState}
            onChange={(e) => this.updateValue(e.checked)}
          />
        )}
      </div>
    );
  }
}
export default GetCheckBox;
