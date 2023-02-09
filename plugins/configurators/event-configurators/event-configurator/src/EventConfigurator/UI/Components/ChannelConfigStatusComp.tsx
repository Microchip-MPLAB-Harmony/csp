import React from 'react';
// import {
//   UpdateSymbolValue,
//   GetSymbolValue,
//   AddSymbolListener,
// } from "Common/SymbolAccess";

import {
  UpdateSymbolValue,
  GetSymbolValue,
  AddSymbolListener,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
// import { globalSymbolSStateData } from 'Common/UIComponents/UIComponentCommonUtils';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
// import { convertToBoolean } from 'Common/Utils';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { PrimeIcons } from 'primereact/api';

interface IProps {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  readOnly: boolean;
  visible: boolean;
}

interface IState {
  symValue?: any;
  readOnlyStatue?: any;
  visibleState?: any;
  styleObjectState?: any;
  classNameState?: any;
}
let obj: ChannelConfigStatusComp | null = null;
class ChannelConfigStatusComp extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      symValue: GetSymbolValue(this.props.componentId, this.props.symbolId),
      readOnlyStatue: this.props.readOnly,
      visibleState: this.props.visible,
    };
    obj = this;
    this.props.symbolListeners.forEach(this.Addlistener);
  }

  Addlistener(value: any) {
    globalSymbolSStateData.set(value, obj);
    AddSymbolListener(value);
  }

  updateValue(event: { value: any }) {
    this.changeValue(event.value);
    UpdateSymbolValue(this.props.componentId, this.props.symbolId, event.value);
  }

  changeValue(value: any) {
    if (this.state.symValue === value) {
      return;
    }
    this.setState({
      symValue: value,
    });
  }

  changeReadOnlyStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.readOnlyStatue === value) {
      return;
    }
    this.setState({
      readOnlyStatue: value,
    });
  }

  changeVisibleStatus(value: any) {
    value = convertToBoolean(value);
    if (this.state.visibleState === value) {
      return;
    }
    this.setState({
      visibleState: value,
    });
  }

  changeStyleState(styleObject: any) {
    this.setState({
      styleObjectState: styleObject,
    });
  }

  changeClassNameState(className: any) {
    if (this.state.classNameState === className) {
      return;
    }
    this.setState({
      classNameState: className,
    });
  }

  changeComponentState(value: any, editable: boolean, visible: boolean) {
    this.changeValue(value);
    this.changeReadOnlyStatus(editable);
    this.changeVisibleStatus(visible);
  }

  getRenderComponent() {
    let fillStyle = { color: 'red' };
    if (this.state.symValue.toLowerCase() === 'true') {
      fillStyle = { color: 'green' };
    }
    return <div className={PrimeIcons.CIRCLE_FILL} style={fillStyle}></div>;
  }

  render() {
    return this.getRenderComponent();
  }
}
export default ChannelConfigStatusComp;
