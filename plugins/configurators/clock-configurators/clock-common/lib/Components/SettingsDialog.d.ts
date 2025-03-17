import { ButtonProps } from 'primereact/button';
interface SettingsProps {
    tooltip: string;
    className: string;
    componentId: string;
    symbolArray: string[];
    dialogWidth: string;
    dialogHeight: string;
}
declare const SettingsDialog: (props: SettingsProps & ButtonProps) => import("react/jsx-runtime").JSX.Element;
export default SettingsDialog;
