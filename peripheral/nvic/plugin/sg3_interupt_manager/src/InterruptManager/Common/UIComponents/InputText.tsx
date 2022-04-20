import { InputText } from "primereact/inputtext";
import React from "react";
import {
  AddSymbolListner,
  GetSymbolValue,
  UpdateSymbolValue,
} from "../SymbolAccess";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  component_id: string;
  symbolId: string;
  symbolListners: any;
  width: string;
  onChange: (arg0: any) => void;
  editable: boolean;
  visible: boolean;
}

interface IState {
  inputTextSelectedValue?: any;
  inputTextEditableState?: boolean;
  inputTextVisibleState?: boolean;
}
let obj: GetInputText | null = null;

class GetInputText extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      inputTextSelectedValue: GetSymbolValue(
        this.props.component_id,
        this.props.symbolId
      ),
      inputTextEditableState: this.props.editable,
      inputTextVisibleState: this.props.visible,
    };
    obj = this;
    this.props.symbolListners.forEach(this.Addlistner);
  }

  Addlistner(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListner(value);
  }

  updateValue(event: { value: any }) {
    UpdateSymbolValue(
      this.props.component_id,
      this.props.symbolId,
      event.value
    );
    this.props.onChange(event);
    this.changeValue(event.value);
  }

  changeValue(value: any) {
    this.setState({
      inputTextSelectedValue: value,
    });
  }

  changeEditableStatus(value: boolean) {
    this.setState({
      inputTextEditableState: value,
    });
  }

  changeComponentState(value: any, editable: boolean, visible: boolean) {
    this.setState({
      inputTextSelectedValue: value,
      inputTextEditableState: editable,
      inputTextVisibleState: visible,
    });
  }

  render() {
    return (
      <div>
        {this.state.inputTextVisibleState && (
          <InputText
            id={this.props.symbolId}
            style={{ width: this.props.width }}
            tooltip={this.state.inputTextSelectedValue}
            value={this.state.inputTextSelectedValue}
            disabled={!this.state.inputTextEditableState}
            onChange={(e) => this.updateValue(e.target)}
          />
        )}
      </div>
    );
  }
}
export default GetInputText;
