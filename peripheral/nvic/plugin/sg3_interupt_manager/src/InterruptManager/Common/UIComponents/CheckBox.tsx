import { Checkbox } from "primereact/checkbox";
import React from "react";
import {
  AddSymbolListner,
  GetSymbolValue,
  UpdateSymbolValue,
} from "../SymbolAccess";
import { convertToBoolean } from "../Utils";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  componentId: any;
  symbolId: any;
  symbolValue: string;
  styleObject: any;
  editable: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  checkBoxstatus?: any;
}

class GetCheckBox extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      checkBoxstatus: convertToBoolean(
        GetSymbolValue(this.props.componentId, this.props.symbolId)
      ),
    };
    globalSymbolSStateData.set(props.symbolId, this);
    AddSymbolListner(props.symbolId);
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

  render() {
    return (
      <div>
        <Checkbox
          id={this.props.symbolId}
          inputId="binary"
          style={this.props.styleObject}
          checked={this.state.checkBoxstatus}
          disabled={!this.props.editable}
          onChange={(e) => this.updateValue(e.checked)}
        />
      </div>
    );
  }
}
export default GetCheckBox;
