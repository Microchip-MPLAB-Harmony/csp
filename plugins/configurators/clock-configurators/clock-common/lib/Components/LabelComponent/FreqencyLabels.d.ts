import ControlInterface from '../../Tools/ControlInterface';
declare const FreqencyLabels: (props: {
    componentId: string;
    boxInfo: ControlInterface[];
    cx: (...classNames: string[]) => string;
    boldLabelStatus?: boolean | undefined;
    redColorForZeroFrequency?: boolean | undefined;
}) => JSX.Element;
export default FreqencyLabels;
