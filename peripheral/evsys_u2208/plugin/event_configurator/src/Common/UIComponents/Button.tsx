import { Button as PrimeButton } from "primereact/button";
import React from "react";
import { convertToBoolean } from "../Utils";
import { globalSymbolSStateData } from "./UIComponentCommonUtils";

interface IProps {
  buttonId: any;
  buttonDisplayText: any;
  tooltip: any;
  tooltipPosition: any;
  readOnly: boolean;
  className: any;
  styleObject: any;
  visible: boolean;
  onChange: (arg0: any) => void;
}

interface IState {
  buttonDisplayValueState?: any;
  buttonReadOnlyState?: boolean;
  buttonVisibleState?: boolean;
  buttonStyleObjectState?: any;
  buttonclassNameState?: any;
}

class Button extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      buttonDisplayValueState: props.buttonDisplayText,
      buttonReadOnlyState: this.props.readOnly,
      buttonVisibleState: this.props.visible,
      buttonStyleObjectState: this.props.styleObject,
      buttonclassNameState: this.props.className,
    };
    globalSymbolSStateData.set(props.buttonId, this);
  }

  updateValue(currentDisplayText: any) {
    this.props.onChange(currentDisplayText);
  }

  changeValue(value: any) {
    this.setState({
      buttonDisplayValueState: value,
    });
  }

  changeReadOnlyStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.buttonReadOnlyState === value) {
      return;
    }
    this.setState({
      buttonReadOnlyState: value,
    });
  }

  changeVisibleStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.buttonVisibleState === value) {
      return;
    }
    this.setState({
      buttonVisibleState: value,
    });
  }

  changeStyleState(styleObject: any) {
    this.setState({
      buttonStyleObjectState: styleObject,
    });
  }

  changeClassNameState(className: any) {
    if (this.state.buttonclassNameState === className) {
      return;
    }
    this.setState({
      buttonclassNameState: className,
    });
  }

  changeComponentState(value: any, readOnly: boolean, visible: boolean) {
    this.changeValue(value);
    this.changeReadOnlyStatus(readOnly);
    this.changeVisibleStatus(visible);
  }

  render() {
    return (
      <div>
        {this.state.buttonVisibleState && (
          <PrimeButton
            type="button"
            className={this.state.buttonclassNameState}
            label={this.state.buttonDisplayValueState}
            tooltip={this.props.tooltip}
            tooltipOptions={{ position: this.props.tooltipPosition }}
            style={this.state.buttonStyleObjectState}
            onClick={(e) =>
              this.props.onChange(this.state.buttonDisplayValueState)
            }
          />
        )}
      </div>
    );
  }
}

export default Button;
