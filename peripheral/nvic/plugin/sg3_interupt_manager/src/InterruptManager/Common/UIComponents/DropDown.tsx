import { Dropdown } from "primereact/dropdown";
import React from "react";
import {
  UpdateSymbolValue,
  AddSymbolListner,
  GetSymbolValue,
} from "../SymbolAccess";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  componentId: any;
  symbolId: any;
  symbolValue: any;
  symbolArray: any;
  styleObject: any;
  editable: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  comboSelectedValue?: any;
}

class GetDropDown extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      comboSelectedValue: GetSymbolValue(
        this.props.componentId,
        this.props.symbolId
      ),
    };
    globalSymbolSStateData.set(props.symbolId, this);
    AddSymbolListner(props.symbolId);
  }

  updateValue(event: { value: any }) {
    this.changeValue(event.value);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, event.value);
    this.props.onChange(event);
  }

  changeValue(value: any) {
    this.setState({
      comboSelectedValue: value,
    });
  }

  render() {
    return (
      <div>
        <Dropdown
          id={this.props.symbolId}
          style={this.props.styleObject}
          value={this.state.comboSelectedValue}
          options={this.props.symbolArray}
          disabled={!this.props.editable}
          onChange={(e) => this.updateValue(e)}
        />
      </div>
    );
  }
}
export default GetDropDown;
