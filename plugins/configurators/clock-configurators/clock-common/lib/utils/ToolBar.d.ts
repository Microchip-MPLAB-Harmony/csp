interface IProps {
    title: string;
    helpUrl: string;
    onClickSummary: () => void;
}
declare const Toolbar: (props: IProps) => JSX.Element;
export default Toolbar;
