interface LabelProps {
  labelName: any;
}

interface CustomLabel {
  labelId: string;
  labelDisplayText: string;
  labelStyle: any;
}

interface CustomLabelWithTooltip {
  labelId: string;
  labelDisplayText: string;
  labelTooltip: string;
  labelStyle: any;
}

export const DisplayLabel: React.FC<LabelProps> = (props): JSX.Element => (
  <>
    <label style={{ fontSize: "14px" }} className="p-col">
      {" "}
      {props.labelName + " "}{" "}
    </label>
  </>
);

export const GetLabelWithCustomDisplay: React.FC<CustomLabel> = (
  props
): JSX.Element => (
  <>
    <label style={props.labelStyle} id={props.labelId}>
      {props.labelDisplayText}
    </label>
  </>
);

export const GetLabelWithCustomDisplayWithTooltip: React.FC<
  CustomLabelWithTooltip
> = (props): JSX.Element => (
  <>
    <label
      style={props.labelStyle}
      id={props.labelId}
      title={props.labelTooltip}
    >
      {props.labelDisplayText}
    </label>
  </>
);
