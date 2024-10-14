import { SymbolProps } from '@mplab_harmony/harmony-plugin-client-lib';
interface LabelProps {
    class: string;
    boldLabelStatus?: boolean;
    tooltip?: string;
    redColorForZeroFrequency?: boolean;
}
declare const IntegerFrequencyLabel: (props: SymbolProps & LabelProps) => import("react/jsx-runtime").JSX.Element;
export default IntegerFrequencyLabel;
