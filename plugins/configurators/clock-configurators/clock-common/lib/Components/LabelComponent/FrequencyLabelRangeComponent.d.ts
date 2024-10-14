import { SymbolProps } from '@mplab_harmony/harmony-plugin-client-lib';
interface LabelProps {
    class: string;
    minValue: number;
    maxValue: number;
    labelTooltip: string;
    boldLabelStatus?: boolean;
}
declare const FrequencyLabelRangeComponent: (props: SymbolProps & LabelProps) => import("react/jsx-runtime").JSX.Element;
export default FrequencyLabelRangeComponent;
