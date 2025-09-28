import streamlit as st

st.title('Tax Calculator-2026')

st.image('https://github.com/yousuf9292/TaxCalculator/blob/main/tax26.PNG?raw=True')

annual_taxable_amount = st.number_input(label="Annual Taxable Amount", placeholder='Enter Taxable Amount')

calculate_slab = st.button("Calculate Tax Slab")

if 'total_yearly_tax' not in st.session_state:
    st.session_state.total_yearly_tax = None

if calculate_slab:
    total_yearly_tax = None

    if annual_taxable_amount <= 600000:
        st.text("No Tax")
        total_yearly_tax = 0

    elif annual_taxable_amount > 600000 and annual_taxable_amount <= 1200000:
        st.text("Tax % As Per Slab: 1.0%")
        taxperappinc = annual_taxable_amount - 600000
        tax_as_per_slab = round((taxperappinc * 1.0) / 100)
        st.text("Tax As Per Slab: " + str(tax_as_per_slab))
        fixed_tax = 0
        total_yearly_tax = tax_as_per_slab + fixed_tax
        st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>', unsafe_allow_html=True)

    elif annual_taxable_amount > 1200000 and annual_taxable_amount <= 2200000:
        st.text("Fixed Tax: 6000")
        st.text("Tax % As Per Slab : 11.0%")
        taxperappinc = annual_taxable_amount - 1200000
        tax_as_per_slab = round((taxperappinc * 11.0) / 100)
        st.text("Tax As Per Slab: " + str(tax_as_per_slab))
        fixed_tax = 6000
        total_yearly_tax = tax_as_per_slab + fixed_tax
        st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>', unsafe_allow_html=True)

    elif annual_taxable_amount > 2200000 and annual_taxable_amount <= 3200000:
        st.text("Fixed Tax: 116,000")
        st.text("Tax % As Per Slab: 23.0%")
        taxperappinc = annual_taxable_amount - 2200000
        tax_as_per_slab = round((taxperappinc * 23.0) / 100)
        st.text("Tax As Per Slab: " + str(tax_as_per_slab))
        fixed_tax = 116000
        total_yearly_tax = tax_as_per_slab + fixed_tax
        st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>', unsafe_allow_html=True)

    elif annual_taxable_amount > 3200000 and annual_taxable_amount <= 4100000:
        st.text("Fixed Tax: 346,000")
        st.text("Tax % As Per Slab: 30.0%")
        taxperappinc = annual_taxable_amount - 3200000
        tax_as_per_slab = round((taxperappinc * 30.0) / 100)
        st.text("Tax As Per Slab: " + str(tax_as_per_slab))
        fixed_tax = 346000
        total_yearly_tax = tax_as_per_slab + fixed_tax
        st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>', unsafe_allow_html=True)

    elif annual_taxable_amount > 4100000:
        st.text("Fixed Tax: 616,000")
        st.text("Tax % As Per Slab: 35%")
        taxperappinc = annual_taxable_amount - 4100000
        tax_as_per_slab = round((taxperappinc * 35.0) / 100)
        st.text("Tax As Per Slab: " + str(tax_as_per_slab))
        fixed_tax = 616000
        total_yearly_tax = tax_as_per_slab + fixed_tax

        super_tax = 0
        if annual_taxable_amount >= 10000000:
            super_tax = round(total_yearly_tax * 0.09)  # 9% super tax
            total_yearly_tax += super_tax

        st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>', unsafe_allow_html=True)
        if super_tax > 0:
            st.markdown(f'<p style=color:red>Super Tax (9%): {str(super_tax)}</p>', unsafe_allow_html=True)

    st.session_state.total_yearly_tax = total_yearly_tax
    # Mark a flag that calculation is done
    st.session_state.slab_calculated = True

# Only show these inputs if slab has been calculated and tax > 0
if st.session_state.get('slab_calculated', False) and st.session_state.total_yearly_tax and st.session_state.total_yearly_tax > 0:

    tax_paid = st.number_input(label="Tax Paid", placeholder='Tax Paid', key='tax_paid')
    number_of_month = st.number_input(label="Number of Months Paid", placeholder='Number of Months', key='number_of_month')

    calculate_monthly = st.button("Calculate Monthly Tax Liability")

    if calculate_monthly:
        if tax_paid > 0 and number_of_month > 0:
            unpaid_month = 12 - number_of_month
            if unpaid_month <= 0:
                st.warning("All months' tax is paid or invalid number of months.")
            else:
                tax_liability = st.session_state.total_yearly_tax - tax_paid
                if tax_liability <= 0:
                    st.success("No tax liability remaining.")
                else:
                    current_month_tax = tax_liability / unpaid_month
                    st.markdown(f"<p style=color:green>Current Month Tax: {round(current_month_tax,3)}</p>", unsafe_allow_html=True)
        else:
            st.info("Please enter valid Tax Paid and Number of Months.")

