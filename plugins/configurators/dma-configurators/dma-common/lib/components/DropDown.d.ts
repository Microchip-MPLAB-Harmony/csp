import React from 'react';
interface IProps {
    componentId: any;
    symbolId: any;
    symbolListeners: any;
    symbolValue: any;
    symbolArray: any;
    styleObject?: any;
    className?: any;
    readOnly: boolean;
    visible: boolean;
    beforeChange?: () => void;
    onChange: (arg0: any) => void;
}
interface IState {
    comboSelectedValue?: any;
    comboReadOnlyStatue?: any;
    comboVisibleState?: any;
    comboStyleObjectState?: any;
    comboclassNameState?: any;
}
declare class DropDown extends React.Component<IProps, IState> {
    constructor(props: IProps);
    componentWillReceiveProps(props: IProps): void;
    Addlistener(value: any): void;
    updateValue(event: {
        value: any;
    }): void;
    changeValue(value: any): void;
    changeReadOnlyStatus(value: any): void;
    changeVisibleStatus(value: any): void;
    changeStyleState(styleObject: any): void;
    changeClassNameState(className: any): void;
    changeComponentState(value: any, editable: boolean, visible: boolean): void;
    render(): JSX.Element;
}
export default DropDown;
