import { Checkbox as PrimeCheckBox } from 'primereact/checkbox';
import React from 'react';
import {
  AddSymbolListener,
  UpdateSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  symbolValue: string;
  styleObject: any;
  className: any;
  readOnly: boolean;
  visible: boolean;
  beforeChange: (arg0: any) => void;
  onChange: (arg0: any) => void;
}

interface IState {
  checkBoxstatus?: any;
  checkBoxReadOnlyState?: boolean;
  checkBoxVisibleState?: boolean;
  checkboxStyleObjectState?: any;
  checkBoxclassNameState?: any;
}
let obj: RecommendedSettingsComp | null = null;

class RecommendedSettingsComp extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.componentWillReceiveProps(this.props);
    // this.state = {
    //   checkBoxstatus: convertToBoolean(this.props.symbolValue),
    //   checkBoxReadOnlyState: this.props.readOnly,
    //   checkBoxVisibleState: this.props.visible,
    //   checkboxStyleObjectState: this.props.styleObject,
    //   checkBoxclassNameState: this.props.className,
    // };
    obj = this;
    this.props.symbolListeners.forEach(this.Addlistener);
  }

  componentWillReceiveProps(nextprops: IProps) {
    this.state = {
      checkBoxstatus: convertToBoolean(nextprops.symbolValue),
      checkBoxReadOnlyState: nextprops.readOnly,
      checkBoxVisibleState: nextprops.visible,
      checkboxStyleObjectState: nextprops.styleObject,
      checkBoxclassNameState: nextprops.className,
    };
  }

  Addlistener(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListener(value);
  }

  updateValue(checked: boolean) {
    this.props.beforeChange(checked);
    this.changeValue(checked);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, checked);
    this.props.onChange(checked);
  }

  changeValue(value: any) {
    value = convertToBoolean(value);
    if (this.state.checkBoxstatus === value) {
      return;
    }
    this.setState({
      checkBoxstatus: value,
    });
  }

  changeReadOnlyStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.checkBoxReadOnlyState === value) {
      return;
    }
    this.setState({
      checkBoxReadOnlyState: value,
    });
  }

  changeVisibleStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.checkBoxVisibleState === value) {
      return;
    }
    this.setState({
      checkBoxVisibleState: value,
    });
  }

  changeStyleState(styleObject: any) {
    this.setState({
      checkboxStyleObjectState: styleObject,
    });
  }

  changeClassNameState(className: any) {
    if (this.state.checkBoxclassNameState === className) {
      return;
    }
    this.setState({
      checkBoxclassNameState: className,
    });
  }

  changeComponentState(value: any, readOnly: boolean, visible: boolean) {
    this.changeValue(value);
    this.changeReadOnlyStatus(readOnly);
    this.changeVisibleStatus(visible);
  }

  render() {
    return (
      <div className={this.state.checkBoxclassNameState}>
        {this.state.checkBoxVisibleState && (
          <PrimeCheckBox
            id={this.props.symbolId}
            inputId="binary"
            style={this.state.checkboxStyleObjectState}
            checked={this.state.checkBoxstatus}
            disabled={this.state.checkBoxReadOnlyState}
            onChange={(e) => this.updateValue(e.checked)}
          />
        )}
      </div>
    );
  }
}
export default RecommendedSettingsComp;
