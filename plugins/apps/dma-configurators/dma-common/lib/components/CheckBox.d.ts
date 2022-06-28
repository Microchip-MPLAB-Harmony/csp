import React from 'react';
interface IProps {
    componentId: any;
    symbolId: any;
    symbolListeners: any;
    symbolValue: string;
    styleObject?: any;
    className?: any;
    readOnly: boolean;
    visible: boolean;
    beforeChange?: () => void;
    onChange: (arg0: any) => void;
}
interface IState {
    checkBoxstatus?: any;
    checkBoxReadOnlyState?: boolean;
    checkBoxVisibleState?: boolean;
    checkboxStyleObjectState?: any;
    checkBoxclassNameState?: any;
}
declare class CheckBox extends React.Component<IProps, IState> {
    constructor(props: IProps);
    componentWillReceiveProps(props: IProps): void;
    Addlistener(value: any): void;
    updateValue(checked: boolean): void;
    changeValue(value: any): void;
    changeReadOnlyStatus(value: any): void;
    changeVisibleStatus(value: any): void;
    changeStyleState(styleObject: any): void;
    changeClassNameState(className: any): void;
    changeComponentState(value: any, readOnly: boolean, visible: boolean): void;
    render(): JSX.Element;
}
export default CheckBox;
