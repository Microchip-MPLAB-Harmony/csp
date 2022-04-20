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
  symbolListners: any;
  symbolValue: any;
  symbolArray: any;
  styleObject: any;
  editable: boolean;
  visible: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  comboSelectedValue?: any;
  comboEditableStatue?: any;
  comboVisibleState?: any;
}
let obj: GetDropDown | null = null;
class GetDropDown extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      comboSelectedValue: GetSymbolValue(
        this.props.componentId,
        this.props.symbolId
      ),
      comboEditableStatue: this.props.editable,
      comboVisibleState: this.props.visible,
    };
    obj = this;
    this.props.symbolListners.forEach(this.Addlistner);
  }

  Addlistner(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListner(value);
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

  changeEditableStatus(value: boolean) {
    this.setState({
      comboSelectedValue: value,
    });
  }

  changeComponentState(value: any, editable: boolean, visible: boolean) {
    this.setState({
      comboSelectedValue: value,
      comboEditableStatue: editable,
      comboVisibleState: visible,
    });
  }

  render() {
    return (
      <div>
        {this.state.comboVisibleState && (
          <Dropdown
            id={this.props.symbolId}
            style={this.props.styleObject}
            value={this.state.comboSelectedValue}
            options={this.props.symbolArray}
            disabled={!this.state.comboEditableStatue}
            onChange={(e) => this.updateValue(e)}
          />
        )}
      </div>
    );
  }
}
export default GetDropDown;
