import { ButtonProps } from 'primereact/button';
interface CustomIconProps {
    tooltip: string;
    className: string;
    icon: string;
    onClick: () => void;
}
export declare const GetIconButton: (props: CustomIconProps & ButtonProps) => import("react/jsx-runtime").JSX.Element;
interface CustomProps {
    label: string;
    className: string;
    tooltip: string;
    onClick: (arg0: any) => void;
}
export declare function GetButton(props: CustomProps & ButtonProps): import("react/jsx-runtime").JSX.Element;
export {};
